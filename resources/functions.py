import resources.lib as lib
import resources.variables as ivars

# def convert_image_to_base64()
def convert_image_to_base64(*, path_image):
    """
        . Recebe o caminho para uma imagem como entrada e retorna a imagem convertida em Base64.

        [INPUT]
            (str) path_image - Caminho onde está localizado a imagem.

        [OUTPUT]
            (obj) image_base64 - Imagem convertida em Base64.
    """

    # Verifica se o STR path_image está vazio
    if not path_image:
        return {'status': -1, 
                'message': "[ERROR] [convert_base64_to_image] - O objeto path_image está vazio. Ele um campo Obrigatório.",
                'obj': None}

    # Verifica se o caminho fornecido corresponde a um arquivo existente.
    if not lib.os.path.isfile(path_image):
        return {'status': -1, 
                'message': f"[ERROR] [convert_image_to_base64] - Caminho da imagem não encontrado: {path_image}",
                'obj': None}
    
    # Converte a imagem em Base64.
    try:
        with open(path_image, 'rb') as image_file:
            image_data   = image_file.read()
            image_base64 = lib.base64.b64encode(image_data)
            return {'status': 1, 
                    'message': '[INFO] [convert_to_base64] - Imagem convertida com sucesso.', 
                    'obj': image_base64}
    
    except IOError as error:        
        return {'status': -1, 
                'message': f'[ERROR] [convert_to_base64] Problema ao abrir ou ler o arquivo: {error}', 
                'obj': None}

# def convert_base64_to_image()
def convert_base64_to_image(*, base, name_image='default_name'):
    """
        . Recebe o objeto Base64 como entrada e retorna o Base64 convertido em Imagem.
 
        [INPUT]
            (obj): base       - Objeto em formato Base64.
            (str): name_image - Nome que a imagem terá após ser convertido.

        [OUTPUT]
            (obj): A imagem convertida em um diretório - image.save(file_img_path)
    """

    # Verifica se o objeto Base64 está vazio
    if not base:
        return {'status': -1, 
                'message': "[ERROR] [convert_base64_to_image] - O objeto Base64 está vazio. Ele um campo Obrigatório.",
                'obj': None}

    # Valida se foi possível realizar a decodificação do Base64.
    try:
        decoded_image = lib.base64.b64decode(base)
    
    except Exception as error:        
        return {'status': -1, 
                'message': f"[ERROR] [convert_base64_to_image] - Problema ao decodificar o Base64: {error}",
                'obj': None}
    
    # Valida a Imagem e sua extensão.
    try:
        image           = lib.Image.open(lib.BytesIO(decoded_image))
        extension_image = image.format.lower()

        # Valida o erro 'cannot write mode P as JPEG'.
        if extension_image.lower() == 'jpeg':
            image = image.convert('RGB')
    
    except Exception as error:
        return {'status': -1, 
                'message': f"[ERROR] [convert_base64_to_image] - Problema ao gerar a imagem: {error}",
                'obj': None}
    
    # Valida a existencia no diretório de imagens retornadas.
    if not lib.os.path.exists(ivars.img_path_output):
        lib.os.makedirs(ivars.img_path_output)
    
    # Salva a imagem no diretório de saida de imagens.
    file_img_path = fr'{ivars.img_path_output}\{name_image}.{extension_image}'
    image.save(file_img_path)
    
    return {'status': 1, 
            'message': f"[INFO] [convert_base64_to_image] - Base64 convertido para imagem com sucesso.",
            'obj': None}
