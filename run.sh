#!/usr/bin/env bash
#set -e
# docker build -t humblehound/pythonparser:latest .
# docker run --rm --name=parser -v /opt/genres/:/app/genres humblehound/pythonparser:latest

#!/usr/bin/env bash
#!/usr/bin/env bash
set -eu

docker run -p 8888:8888 -v $(pwd):/notebooks -it --rm pcej/keras-jupyter-yaafe    