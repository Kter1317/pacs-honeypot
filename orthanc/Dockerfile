FROM debian:bullseye

# 安裝 Orthanc 執行所需依賴
RUN apt-get update && apt-get install -y \
    libcurl4 \
    libsqlite3-0 \
    libdcmtk-dev \
    libboost-all-dev \
    libjsoncpp-dev \
    liblua5.3-0 \
    libjpeg62-turbo \
    && ln -s /lib/x86_64-linux-gnu/libjpeg.so.62 /lib/x86_64-linux-gnu/libjpeg.so.8 \
    && rm -rf /var/lib/apt/lists/*

# 複製主程式
COPY bin/Orthanc /usr/sbin/Orthanc

# 複製整個設定資料夾（config/ 對應 /etc/orthanc/）
COPY config/ /etc/orthanc/

# 複製 plugin
COPY plugins/ /usr/share/orthanc/plugins/

# 預設啟動命令
CMD ["/usr/sbin/Orthanc", "/etc/orthanc/orthanc.json"]
