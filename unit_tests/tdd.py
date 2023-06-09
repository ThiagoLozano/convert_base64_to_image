import sys
sys.path.append('./')

import resources.functions as function

# convert_image_to_base64()
def test_convert_image_to_base64():
    tests_case = [

        # 1. Testa o caso em que o caminho da imagem existe.
        {
            "num_test": 1,
            "path":r"C:\Users\Acer\Desktop\Convert_Image_to_base64\img_input\red_hot.png",
            "expected_return": 1
        },

        # 2. Testa o caso em que o caminho da imagem não existe.
        {   
            "num_test": 2,
            "path":r'C:\Users\Acer\Desktop\Convert_Image_to_base64\img_input\test_error.png',
            "expected_return": -1
        },

        # 3. Testa o caso em que o caminho fornecido não é um arquivo válido.
        {
            "num_test": 3,
            "path":"",
            "expected_return": -1
        },

        # 4. Testa o caso em que ocorre um erro de E/S (por exemplo, o arquivo não pode ser lido).
        {
            "num_test": 4,
            "path":r"path/invalid/image.png",
            "expected_return": -1
        }
    ]
    
    for case in tests_case:
        try:
            result = function.convert_image_to_base64(path_image=case['path'])
            assert result['status'] == case['expected_return']

            print(f"[test_convert_image_to_base64] [INFO] - Passou no Teste Nº: {case['num_test']}")

        except AssertionError:
            print(f"[test_convert_image_to_base64] [ERROR] - Não Passou no Teste Nº: {case['num_test']} | Retornou os status: {result['status']} e Esperava status: {case['expected_return']})")

# convert_base64_to_image()
def test_convert_base64_to_image():
    tests_case = [

        # 1. Testa o caso em que Base64 e sua extensão estão corretos.
        {   
            "num_test": 1,
            "base": b'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',
            "name_image": "default_name",
            "expected_return": 1
        },

        # 2. Testa o caso em que Base64 está incorreto.
        {   
            "num_test": 2,
            "base": b"invalid_base64_data",
            "name_image": "default_name2",
            "expected_return": -1
        },

        # 3. Testa o caso em que que Base64 está vazio.
        {   
            "num_test": 3,
            "base": "",
            "name_image": "default_name3",
            "extension_image": "png",
            "expected_return": -1
        }
    ]

    for case in tests_case:
        try:
            result = function.convert_base64_to_image(base=case['base'], name_image=case['name_image'])
            
            assert result['status'] == case['expected_return']

            print(f"[test_convert_base64_to_image] [INFO] - Passou no Teste Nº: {case['num_test']}")

        except AssertionError:
            print(f"[test_convert_base64_to_image] [ERROR] - Não Passou no Teste Nº: {case['num_test']} | Retornou os status: {result['status']} e Esperava status: {case['expected_return']})")

# Inicializa os testes aqui.
# test_convert_image_to_base64()
# test_convert_base64_to_image()
