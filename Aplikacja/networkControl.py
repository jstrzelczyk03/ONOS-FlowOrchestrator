import networkx as nx
import requests
import matplotlib.pyplot as plt


def create_graph(my_file):
    """
    Creates a network topology graph based on the information in the specified file.
    :param my_file: path to the file containing network topology information.
    :return: network topology graph representing the connections between hosts

    File Format:
    The file should have the following format:
    - The first line contains a comma-separated list of host names.
    - Subsequent lines contain comma-separated values representing connections between hosts:
      host1, host2, delay, bandwidth, port_host1, port_host2
    """
    topo = nx.Graph()

    with open(my_file, "r") as file:
        hosts = file.readline().strip().split(",")
        links = []

        for line in file.readlines():
            line = line.strip().split(",")
            host1, host2, delay, bandwidth = line[0], line[1], float(line[2]), float(line[3])
            ports_dict = {host1: int(line[4]), host2: int(line[5])}
            params = {'delay': delay, 'bandwidth': bandwidth, 'ports': ports_dict}
            link = host1, host2, params
            links.append(link)

    topo.add_nodes_from(hosts)
    topo.add_edges_from(links)
    # pos = nx.spring_layout(topo)
    # nx.draw(topo, pos, with_labels=True, font_weight='bold')
    # edge_labels = {(u, v): f"d: {d['delay']}, b: {d['bandwidth']}" for u, v, d in topo.edges(data=True)}
    # nx.draw_networkx_edge_labels(topo, pos, edge_labels=edge_labels)
    # plt.show()

    return topo


network_topology = create_graph('topology.txt')


def create_json(min_path, i):
    """
    Creates a JSON file to configure nodes of a network based on the given minimum path.
    :param min_path: The minimum path found in the algorithm, represented as a list of nodes
    :param i:  A number used to create a unique filename for the JSON file.
    :return: JSON file with configuration information
    """
    json_ = "{\"flows\": ["

    with open("Onos" + str(i) + ".json", "w") as file1:
        with open('OnosInput.json', "r") as file:
            json = file.read()

        h0 = min_path[0]
        h_end = min_path[len(min_path) - 1]

        js = json.replace('%1', h0[1])
        js = js.replace('%2', "1")
        js = js.replace('%3', h0[1])
        js = js.replace('%4', h_end[1])
        js = js.replace('%5', "1")
        js = js.replace('%6', h_end[1])
        json_ += js + ","

        for i in range(0, len(min_path) - 1):
            h_act = min_path[i]
            h_next = min_path[i + 1]
            port_act = network_topology.get_edge_data(h_act, h_next)['ports'][h_act]
            port_next = network_topology.get_edge_data(h_act, h_next)['ports'][h_next]
            js = json.replace('%1', h_act[1])
            js = js.replace('%2', str(port_act))
            js = js.replace('%3', h_end[1])
            js = js.replace('%4', h_next[1])
            js = js.replace('%5', str(port_next))
            js = js.replace('%6', h0[1])
            json_ = json_ + js + ","

        json_ = json_[:-2]
        json_ += "}]}"
        file1.write(json_)


def user_input():
    """
    Enables the user to input network connections.
    :return: Dictionary containing parameters of the connections: {index: [first_host, second_host, data_stream_size]}
    """
    connections = {}
    try:
        still_continue = True
        i = 0
        while still_continue:
            hx = input("Podaj pierwszego hosta: ")
            hy = input("Podaj drugiego hosta: ")
            size = input("Podaj wielkość strumienia danych [Mbit/s]: ")

            if size == "":
                # the default value is 1Mbps
                size = 1
            else:
                size = float(size)

            connection = [hx, hy, size]
            connections[i] = connection
            i += 1

            if_continues = input("Czy zakończyć wprowadzanie połączeń ['y', 'n']: ").lower()
            if if_continues == "y":
                still_continue = False

    except ValueError:
        print("Błąd! Wprowadź poprawne dane liczbowe dla wielkości strumienia danych.")
        return None

    print("Wprowadzone połączenia:")
    for index, connection in connections.items():
        print(
            f"{index + 1}. Host {connection[0]} <-> Host {connection[1]}, Wielkość strumienia danych: {connection[2]} Mbit/s")
    return connections


def find_all_paths(first_host, second_host):
    """
    Finds all paths between two hosts in the network topology.
    :param first_host: The starting host
    :param second_host: The destination host
    :return: A list containing all paths between the two specified hosts. Each path is represented as a list of nodes
    """
    all_paths = list(nx.all_simple_paths(network_topology, source=first_host, target=second_host))
    all_paths.sort(key=lambda path: calculate_total_delay(path))
    return all_paths


def find_path(all_paths, flow_rate):
    """
    Finds the favorable path based on available bandwidth from a list of paths.
    :param all_paths: A list of all paths
    between two hosts.
    :param flow_rate: The stream size to send in one second [Mbps]

    The function looks at all paths between two hosts, which are ordered by the lowest summed delay. First,
    it looks for a path for which the minimum link bandwidth is greater than the connection flow rate and at the same
    time the delay is as small as possible. If there is no such path, it takes the path that has the highest possible
    bandwidth, but if there are several paths with the same bandwidth, it takes the one with the lowest delay.
    """
    min_bandwidth_path = []
    best_path = []

    for path in all_paths:
        len_of_path = len(path)
        min_bandwidth = network_topology.get_edge_data(path[0], path[1])['bandwidth']

        for i in range(1, len_of_path - 1):
            if network_topology.get_edge_data(path[i], path[i + 1])['bandwidth'] < min_bandwidth:
                min_bandwidth = network_topology.get_edge_data(path[i], path[i + 1])['bandwidth']
        min_bandwidth_path.append(min_bandwidth)
    if_found = False

    for i in range(len(min_bandwidth_path)):
        if min_bandwidth_path[i] > flow_rate:
            best_path = all_paths[i]
            if_found = True
            break

    if not if_found:
        max_band = 0

        for flow_rate in min_bandwidth_path:
            if flow_rate > max_band:
                max_band = flow_rate

        for i in range(len(min_bandwidth_path)):
            if min_bandwidth_path[i] == max_band:
                best_path = all_paths[i]
                break

    print("Znaleziona ścieżka: " + str(best_path))
    return best_path


def calculate_total_delay(path):
    """
    Calculates the total delay along a given path in the network topology.
    The function iterates through the nodes in the path and accumulates the delay of each edge.
    :param path: A list of nodes representing the path
    :return: The total delay along the specified path
    """
    total_delay = 0

    for i in range(len(path) - 1):
        edge_delay = network_topology.get_edge_data(path[i], path[i + 1])['delay']
        total_delay += edge_delay

    return total_delay


def change_topology(found_path, band):
    """
    After finding a path in the algorithm, updates the bandwidth values of the links in the network topology.
    :param found_path: The path found by the algorithm.
    :param band: The flow rate of the connection.
    """
    for i in range(0, len(found_path) - 1):
        network_topology[found_path[i]][found_path[i + 1]]['bandwidth'] -= (band + 5)


def post_json_files():
    """
    Generates and posts JSON files for configuring network nodes based on user input.
    """
    if_sent = True
    params = user_input()
    amount_of_connections = len(params.keys())

    for i in range(amount_of_connections):
        hx = params[i][0]
        hy = params[i][1]
        band = params[i][2]
        paths = find_all_paths(hx, hy)
        found_path = find_path(paths, band)
        change_topology(found_path, band)
        create_json(found_path, i)

        with open("Onos" + str(i) + ".json", "r") as file:
            onos_json = file.read()

        url_post = "http://192.168.0.80:8181/onos/v1/flows"

        headers = {
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

        response = requests.post(url_post, data=onos_json, headers=headers, auth=("onos", "rocks"))

        if response.status_code != 200:
            if_sent = False

    if if_sent:
        print("Wszystkie pliki zostały pomyślnie przesłane do kontrolera.")


post_json_files()
