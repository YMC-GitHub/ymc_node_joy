# Standard library imports
import os
import json

# Third-party imports
import folder_paths
import torch
from transformers import AutoProcessor

# def get_torch_device():  
#     """  
#     返回PyTorch模型应该运行的设备（CPU或GPU）  
#     如果系统支持CUDA并且至少有一个GPU可用，则返回GPU设备；否则返回CPU设备。  
#     """  
#     if torch.cuda.is_available():  
#         # 选择第一个可用的GPU  
#         device = torch.device("cuda:0")  
#         print(f"There are {torch.cuda.device_count()} GPU(s) available.")  
#         print(f"We will use the GPU: {device}")  
#     else:  
#         # 如果没有GPU可用，则使用CPU  
#         device = torch.device("cpu")  
#         print("No GPU available, using the CPU instead.")  
#     return device

def get_comfyui_models_dir() -> str:
    """
    Get ComfyUI models directory path by traversing up from current custom nodes directory
    
    Returns:
        str: Absolute path to ComfyUI models directory
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Traverse up 3 levels from custom_nodes to reach ComfyUI root
    comfyui_root = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))
    models_dir = os.path.join(comfyui_root, 'models')
    
    if not os.path.exists(models_dir):
        raise FileNotFoundError(f"ComfyUI models directory not found at: {models_dir}")
        
    return models_dir

# 下载hg 模型到本地
def download_hg_model(model_id:str,exDir:str=''):
    # 下载本地
    model_checkpoint = os.path.join(folder_paths.models_dir, exDir, os.path.basename(model_id))
    print(model_checkpoint)
    if not os.path.exists(model_checkpoint):
        from huggingface_hub import snapshot_download
        snapshot_download(repo_id=model_id, local_dir=model_checkpoint, local_dir_use_symlinks=False)
    return model_checkpoint