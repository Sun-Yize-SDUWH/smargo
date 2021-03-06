import os

from tqdm import tqdm

from smargo.loader import convert_go_sgf, dump_json, load_sgf
from smargo.visualize import plot_go_file

# info = load_sgf('data/sgf/tsumego_000000.sgf')
# dump_json(info, 'data/test1.json')

load_path = "output/download/"
dump_path = "smargo_50/"
convert_go_sgf(load_path, dump_path)

for file in tqdm(sorted([_ for _ in os.listdir(dump_path + "json") if _.endswith(".json")])):
    plot_go_file(os.path.join(dump_path, "json", file))
