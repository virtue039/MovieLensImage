# MovieLensImage

MovieLensImage 是一个用于从 IMDb 官方网站抓取电影图片的爬虫。它专门针对 MovieLens 25M 数据集中列出的电影，并提供了正常运行和多线程运行两种方式。

## 描述

MovieLensImage 获取 IMDb 上的电影海报和相关图片，确保用户可以收集 MovieLens 25M 数据集中的电影的全面视觉资料。项目包含两个主要脚本和一个压缩包：
- `spider.py`: 正常运行的爬虫脚本。
- `thread.py`: 多线程运行的爬虫脚本，用于加速抓取过程。

### 特性

- 根据 MovieLens 25M 数据集抓取电影图片。
- 提供单线程和多线程抓取两种模式。
- 更新白名单和黑名单，分别记录成功和失败的抓取。
- 使用代理 IP 池以避免被 IMDb 屏蔽。

### 项目结构

- `spider.py`: 主要爬虫脚本。
- `thread.py`: 多线程爬虫脚本。
- `white_black_file/`: 存储白名单和黑名单的目录。
- `useful_ip.txt`: 包含代理 IP 的文件。


## 技术栈

- Python 3.6 或更高版本
- 代理 IP 池（具体参考[ProxyPool](https://github.com/Python3WebSpider/ProxyPool.git)）
- 用于 HTML 解析的 BeautifulSoup
- 用于处理 HTTP 请求的 Requests 库
- 用于多线程抓取的 Threading 库


## 技术说明

### 安装

1. 克隆仓库:
    ```bash
    git clone https://github.com/yourusername/MovieLensImage.git
    cd MovieLensImage
    ```

2. 创建虚拟环境:
    ```bash
    python -m venv venv
    source venv/bin/activate  # 在 Windows 上使用 `venv\Scripts\activate`
    ```

3. 安装所需包:
    ```bash
    pip install -r requirements.txt
    ```

4. 提供两种IP代理方案：
   1. 根据 [此处](https://github.com/Python3WebSpider/ProxyPool.git) 的说明配置动态 IP 池。
   2. 使用useful_ip.txt。注：IP不稳定，会失效

### 下载数据集

- 从 [百度网盘](https://pan.baidu.com/s/1btpbCDTY5LVaGG5aKtnOYA?pwd=slyr) 下载 MovieLens 25M 数据集，提取码为 `slyr`。

### 运行爬虫

#### 正常运行

运行单线程爬虫:
```bash
python spider.py
```

#### 多线程运行

运行多线程爬虫:
```bash
python thread.py
```

### 许可证

本项目基于 MIT 许可证。详情请参阅 LICENSE 文件。


# MovieLensImage

MovieLensImage is a crawler for scraping movie images from the official IMDb website. It specifically targets movies listed in the MovieLens 25M dataset and provides both normal and multi-threaded modes.

## Description

MovieLensImage fetches movie posters and related images on IMDb, ensuring that users can collect comprehensive visual information about movies in the MovieLens 25M dataset. The project contains two main scripts and a compressed package:
- `spider.py`: The normal crawler script.
- `thread.py`: The multi-threaded crawler script to speed up the scraping process.
- ``

### Features

- Crawling movie images based on the MovieLens 25M dataset.
- Providing single-threaded and multi-threaded scraping modes.
- Update whitelist and blacklist to record successful and failed scraping respectively.
- Use proxy IP pool to avoid being blocked by IMDb.

### Project Structure

- `spider.py`: The main crawler script.
- `thread.py`: multi-threaded crawler script.
- `white_black_file/`: directory for storing whitelist and blacklist.
- `useful_ip.txt`: file containing proxy IP.

## Technology stack

- Python 3.6 or higher
- Proxy IP pool (see [ProxyPool](https://github.com/Python3WebSpider/ProxyPool.git) for details)
- BeautifulSoup for HTML parsing
- Requests library for processing HTTP requests
- Threading library for multi-threaded crawling

## Technical description

### Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/MovieLensImage.git
cd MovieLensImage
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate # Use `venv\Scripts\activate` on Windows
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

4. Provide two IP proxy solutions:
   1. According to Configure a dynamic IP pool according to the instructions [here](https://github.com/Python3WebSpider/ProxyPool.git).
   2. Use useful_ip.txt. Note: IP is unstable and will become invalid

### Download the dataset

- Download the MovieLens 25M dataset from [Baidu Netdisk](https://pan.baidu.com/s/1btpbCDTY5LVaGG5aKtnOYA?pwd=slyr), the extraction code is `slyr`.

### Run the crawler

#### Normal operation

Run a single-threaded crawler:
```bash
python spider.py
```

#### Multi-threaded operation

Run a multi-threaded crawler:
```bash
python thread.py
```

### License

This project is based on the MIT license. See the LICENSE file for details.