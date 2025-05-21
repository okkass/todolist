FROM python:3.12

# UID、GIDの設定(どうせdevcontainer.jsonで上書きされるが、念のためのデフォルト値)
ARG USERNAME=vscode
ARG USER_UID=1000
ARG USER_GID=1000

# 更新
RUN pip install --upgrade pip

# ユーザーとグループの作成
RUN groupadd --gid ${USER_GID} ${USERNAME} \
    && useradd --uid ${USER_UID} --gid ${USER_GID} -m ${USERNAME}
WORKDIR /app

COPY src/requirements.txt .
RUN pip install -r requirements.txt

USER ${USERNAME}

CMD ["python", "src/main.py"]