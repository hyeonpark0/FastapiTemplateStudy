FROM python:3.10.4

WORKDIR /code

# Update pip
RUN pip install --upgrade pip

# Copy resources
COPY . /code

# Install requirements (prod/dev)
RUN pip install --no-cache-dir --upgrade -r /code/requirements-dev.txt

# Install app CLI
WORKDIR /code/cli
RUN poetry build
RUN pip install --no-cache-dir --upgrade dist/cli-0.1.0-py3-none-any.whl
ENV PATH="${PATH}:/root/.local/bin"

# Expose port
EXPOSE 80
WORKDIR /code

# Execution command
ENTRYPOINT ["app-cli", "run", "--env", "docker"]
