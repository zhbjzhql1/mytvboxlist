import json
import os
import argparse

def merge_json_files(input_dir, output_file, overwrite=True):
    merged_data = {}

    # 遍历输入目录下的所有文件
    for filename in os.listdir(input_dir):
        if filename.endswith(".json"):
            file_path = os.path.join(input_dir, filename)
            
            # 读取JSON文件
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            
            # 合并数据
            for key, value in data.items():
                if key in merged_data:
                    # 如果键已存在且不想覆盖，则将新值添加到列表中
                    if not overwrite:
                        if isinstance(merged_data[key], list):
                            merged_data[key].append(value)
                        else:
                            merged_data[key] = [merged_data[key], value]
                    else:
                        # 否则，直接覆盖旧值
                        merged_data[key] = value
                else:
                    merged_data[key] = value

    # 将合并后的数据写入输出文件
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(merged_data, f, ensure_ascii=False, indent=4)

    print(f"Merged JSON files successfully and saved to {output_file}")

if __name__ == "__main__":
    # 解析命令行参数
    parser = argparse.ArgumentParser(description="Merge multiple JSON files into one.")
    parser.add_argument("input_dir", type=str, help="The directory containing the JSON files to merge.")
    parser.add_argument("output_file", type=str, help="The file to save the merged JSON data to.")
    parser.add_argument("--no-overwrite", action="store_false", dest="overwrite", help="Do not overwrite existing keys in the merged data.")
    
    args = parser.parse_args()

    # 检查输入目录是否存在
    if not os.path.isdir(args.input_dir):
        print(f"Error: The directory '{args.input_dir}' does not exist.")
        exit(1)

    # 调用合并函数
    merge_json_files(args.input_dir, args.output_file, args.overwrite)