'''Get camera config file from server module'''

import requests
import json

def get_camera_config():
    # 클라우드 서버의 URL 및 JSON 파일 경로 설정
    server_url = 'http://클라우드서버주소'
    json_path = '/camera_config.json'

    # HTTP GET 요청 수행
    try:
        response = requests.get(server_url + json_path)
        response.raise_for_status()  # HTTP 오류가 발생하면 예외 발생
    except requests.exceptions.RequestException as e:
        print(f"Error during HTTP request: {e}")
        return None

    # JSON 데이터 파싱
    try:
        camera_config = response.json()
        return camera_config
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        return None

if __name__ == "__main__":
    # 부팅 시 실행할 코드
    camera_config = get_camera_config()

    if camera_config is not None:
        print("Camera Configuration:")
        print(json.dumps(camera_config, indent=2))
    else:
        print("Failed to retrieve camera configuration.")