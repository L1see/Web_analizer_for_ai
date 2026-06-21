from flask import Flask, render_template, url_for, request

app = Flask(__name__)

def gpu_memory(gpu_name):
    gpu_name = gpu_name.lower()
    gpu_base = {
        'rtx 4090': 24,
        'rtx 4080': 16,
        'rtx 4070 ti': 12,
        'rtx 4070': 12,
        'rtx 4060 ti': 8,
        'rtx 4060': 8,

        'rtx 3090': 24,
        'rtx 3080 ti': 12,
        'rtx 3080': 10,
        'rtx 3070 ti': 8,
        'rtx 3070': 8,
        'rtx 3060 ti': 8,
        'rtx 3060': 12,
        'rtx 3050': 8,

        'rtx 2080 ti': 11,
        'rtx 2080': 8,
        'rtx 2070': 8,
        'rtx 2060': 6,

        'gtx 1660 ti': 6,
        'gtx 1660': 6,
        'gtx 1650': 4,
        'gtx 1080 ti': 11,
        'gtx 1080': 8,
        'gtx 1070': 8,
        'gtx 1060': 6,

        'rx 7900 xtx': 24,
        'rx 7900 xt': 20,
        'rx 7800 xt': 16,
        'rx 7700 xt': 12,
        'rx 7600': 8,

        'rx 6900 xt': 16,
        'rx 6800 xt': 16,
        'rx 6800': 16,
        'rx 6700 xt': 12,
        'rx 6600 xt': 8,
        'rx 6600': 8,
    }
    for gpu, vram in gpu_base.items():
        if gpu in gpu_name:
            return vram
    return 0


def cpu_memory(cpu_name):
    cpu_name = cpu_name.lower()
    cpu_base = {
        'i9-14900k': 24,
        'i9-13900k': 24,
        'i9-12900k': 16,
        'i7-14700k': 20,
        'i7-13700k': 16,
        'i7-12700k': 12,
        'i5-14600k': 14,
        'i5-13600k': 14,
        'i5-12600k': 10,
        'i7-1360u': 10,
        'i7-1355u': 10,
        'i5-1335u': 10,

        'ryzen 9 7950x': 16,
        'ryzen 9 7900x': 12,
        'ryzen 9 5950x': 16,
        'ryzen 7 7800x3d': 8,
        'ryzen 7 7700x': 8,
        'ryzen 7 5800x': 8,
        'ryzen 5 7600x': 6,
        'ryzen 5 7500f': 6,
        'ryzen 5 5600x': 6,
        'ryzen 7 7840u': 8,
        'ryzen 7 5800u': 8,
        'ryzen 5 7640u': 6,
    }
    for cpu, vram in cpu_base.items():
        if cpu in cpu_name:
            return vram
    return 0

def ai_gpu_memory(gpu_mem):
    gpu_base = [
        ['llama 3.2 1b', 1.5],
        ['gemma 2 2b', 2],
        ['llama 3.2 3b', 2.5],
        ['qwen 2.5 3b', 2.5],
        ['llama 3.1 8b', 6],
        ['qwen 2.5 7b', 5.5],
        ['mistral 7b', 5.5],
        ['gemma 2 9b', 6.5],
        ['yi 1.5 9b', 6.5],
        ['falcon 2 11b', 8],
        ['phi-4 14b', 9.5],
        ['qwen 2.5 14b', 9.5],
        ['starcoder2 15b', 10],
        ['deepseek coder v2 lite 16b', 11],
        ['gemma 2 27b', 18],
        ['qwen 2.5 32b', 21],
        ['yi 1.5 34b', 22],
        ['command r 35b', 22],
        ['mixtral 8x7b', 28],
        ['qwen2-vl 7b', 6.5],
        ['llava v1.6 13b', 9],
        ['whisper large v3', 3],
        ['stable diffusion 3.5 medium', 10],
        ['llama 3.1 70b', 42],
        ['qwen 2.5 72b', 44]
    ]
    available_models = []
    for i in range(len(gpu_base)): # функция поиска модели по количеству оперативной памяти видеокарты
        if gpu_mem >= gpu_base[i][1]:
            available_models.append(gpu_base[i][0])
    return available_models

def ai_ram_memory(ram_mem):
    ram_base = [
        ['llama 3.2 1b', 4],
        ['gemma 2 2b', 4],
        ['llama 3.2 3b', 6],
        ['qwen 2.5 3b', 6],
        ['llama 3.1 8b', 12],
        ['qwen 2.5 7b', 12],
        ['mistral 7b', 12],
        ['gemma 2 9b', 14],
        ['yi 1.5 9b', 14],
        ['falcon 2 11b', 14],
        ['phi-4 14b', 16],
        ['qwen 2.5 14b', 16],
        ['starcoder2 15b', 16],
        ['deepseek coder v2 lite 16b', 18],
        ['gemma 2 27b', 28],
        ['qwen 2.5 32b', 32],
        ['yi 1.5 34b', 32],
        ['command r 35b', 32],
        ['mixtral 8x7b', 40],
        ['qwen2-vl 7b', 12],
        ['llava v1.6 13b', 16],
        ['whisper large v3', 8],
        ['stable diffusion 3.5 medium', 16],
        ['llama 3.1 70b', 64],
        ['qwen 2.5 72b', 64]
    ]
    available_models = []
    for i in range(len(ram_base)): # функция поиска модели по количеству оперативной памяти
        if ram_mem >= ram_base[i][1]:
            available_models.append(ram_base[i][0])
    return available_models

def ai_cpu_memory(cpu_cores):
    cpu_base = [
        ['llama 3.2 1b', 1],
        ['gemma 2 2b', 1.5],
        ['llama 3.2 3b', 2],
        ['qwen 2.5 3b', 2],
        ['llama 3.1 8b', 5],
        ['qwen 2.5 7b', 5],
        ['mistral 7b', 5],
        ['gemma 2 9b', 6],
        ['yi 1.5 9b', 6],
        ['falcon 2 11b', 7],
        ['phi-4 14b', 9],
        ['qwen 2.5 14b', 9],
        ['starcoder2 15b', 9],
        ['deepseek coder v2 lite 16b', 10],
        ['gemma 2 27b', 17],
        ['qwen 2.5 32b', 20],
        ['yi 1.5 34b', 21],
        ['command r 35b', 21],
        ['mixtral 8x7b', 26],
        ['qwen2-vl 7b', 6],
        ['llava v1.6 13b', 8],
        ['whisper large v3', 3],
        ['stable diffusion 3.5 medium', 12],
        ['llama 3.1 70b', 40],
        ['qwen 2.5 72b', 42]
    ]
    available_models = []
    for i in range(len(cpu_base)): # функция поиска модели по количеству оперативной памяти
        if cpu_cores >= cpu_base[i][1]:
            available_models.append(cpu_base[i][0])
    return available_models

# список всех моделей для начального отображения
all_models = sorted([
    'llama 3.2 1b', 'gemma 2 2b', 'llama 3.2 3b', 'qwen 2.5 3b',
    'llama 3.1 8b', 'qwen 2.5 7b', 'mistral 7b', 'gemma 2 9b',
    'yi 1.5 9b', 'falcon 2 11b', 'phi-4 14b', 'qwen 2.5 14b',
    'starcoder2 15b', 'deepseek coder v2 lite 16b', 'gemma 2 27b',
    'qwen 2.5 32b', 'yi 1.5 34b', 'command r 35b', 'mixtral 8x7b',
    'qwen2-vl 7b', 'llava v1.6 13b', 'whisper large v3',
    'stable diffusion 3.5 medium', 'llama 3.1 70b', 'qwen 2.5 72b'
])

@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        pc_config = []
        confirmed_matches = []

        cpu = request.form['cpu']
        gpu = request.form['gpu']
        ram = request.form['ram']

        pc_config.append(cpu_memory(cpu))
        pc_config.append(gpu_memory(gpu))
        pc_config.append(int(ram))

        allowed_by_cpu = ai_cpu_memory(pc_config[0])
        allowed_by_gpu = ai_gpu_memory(pc_config[1])
        allowed_by_ram = ai_ram_memory(pc_config[2])

        confirmed_matches = list(set(allowed_by_cpu) & set(allowed_by_gpu) & set(allowed_by_ram))
        confirmed_matches.sort()

        return render_template('index.html',
                               confirmed_matches=confirmed_matches,
                               cpu=cpu, gpu=gpu, ram=ram,
                               all_models=all_models)

    return render_template('index.html', all_models=all_models) # команда на создание слова

if __name__ == '__main__': # вывод кода
    app.run(debug=True) # команда на вывод ошибки