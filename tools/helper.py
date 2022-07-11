import psutil
import torch
import nvsmi


# RCC
# ssh midway2.rcc.uchicago.edu -l mingyuliu -p 22
# module load python
# module load cuda/11.2
# sinteractive --partition=gpu2 --gres=gpu:1 --time=36:00:00

# Risklab
# ssh risklab.chicagobooth.edu -l mingyuliu -p 22
# tmux attach -t ml_prediction
# conda activate ml_prediction

# check CUDA
print(f"CUDA version: {torch.version.cuda}")
print(f"GPU availability: {torch.cuda.is_available()}")
print(f"GPU counts: {torch.cuda.device_count()}")

# check memory and CPU usage
# mpstat -P ALL 1
print(f"CPU usage: {psutil.cpu_percent()}")
print(f"Mem usage: {psutil.virtual_memory().percent}")

# check GPU usage
print(list(nvsmi.get_gpus())[0])
print(list(nvsmi.get_gpus())[1])
