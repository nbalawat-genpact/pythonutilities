.\venv\Scripts\activate
python -m pip install --upgrade seaborn
pip install -r requirements.txt
python -c "import tensorflow as tf;print(tf.reduce_sum(tf.random.normal([1000, 1000])))"
pip install https://storage.googleapis.com/tensorflow/windows/cpu/tensorflow_cpu-2.1.0-cp36-cp36m-win_amd64.whl
pip install jupyterlab

