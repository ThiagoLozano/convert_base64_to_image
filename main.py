import resources.functions as function
import resources.variables as ivars

# =============================
#  Converte a imagem em Base64
# =============================

img_input = ivars.img_path_input

conversao_para_base64 = function.convert_image_to_base64(path_image=img_input)

if conversao_para_base64['status'] == 1:
    print(conversao_para_base64['message'])
    base_64 = conversao_para_base64['obj']

elif conversao_para_base64['status'] == -1:
    print(conversao_para_base64['message'])

# =============================
#  Converte o Base64 em imagem
# =============================

convercao_para_imagem = function.convert_base64_to_image(base=base_64, name_image='teste')

if convercao_para_imagem['status'] == 1:
    print(convercao_para_imagem['message'])

elif convercao_para_imagem['status'] == -1:
    print(convercao_para_imagem['message'])
