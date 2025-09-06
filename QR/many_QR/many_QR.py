import qrcode
import re

file_path = r'Study\QR\many_QR\link.txt'
with open(file_path, 'rt', encoding='UTF8') as f:
    read = f.readlines()

    for line in read:
        line = line.strip()
        print(line)
        
        qr_data = line
        qr_img = qrcode.make(qr_data)
        
        # 특수 문자를 언더바(_)로 대체하여 파일 이름으로 사용 가능한 문자열로 만듭니다.
        safe_filename = re.sub(r'[^a-zA-Z0-9가-힣\s]', '_', qr_data)
        
        save_path = r'Study\QR\many_QR\\' + safe_filename + '.png'
        
        try:
            qr_img.save(save_path)
            print(f"QR 코드 저장 성공: {save_path}")
        except OSError as e:
            print(f"오류 발생: {e} - 파일 이름에 유효하지 않은 문자가 포함되어 있을 수 있습니다.")