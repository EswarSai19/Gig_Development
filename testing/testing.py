import requests
import xmltodict

def fetch_image_keys():
    try:
        url = "https://pl3jxdg8e2.execute-api.ap-south-1.amazonaws.com/Sandbox/jobs-sec1-ads"
        cdn_base_url = "https://dxcln6pws6tir.cloudfront.net/"

        # Fetch the XML data
        response = requests.get(url)
        response.raise_for_status()

        # Parse XML to dictionary
        data = xmltodict.parse(response.text)

        # Extract keys
        contents = data.get('ListBucketResult', {}).get('Contents', [])
        
        # Ensure contents is a list
        if not isinstance(contents, list):
            contents = [contents]

        keys = [item['Key'] for item in contents]

        print(keys)  # Output the extracted keys
        for key in keys:
            print(cdn_base_url + key)

        return keys
    except requests.RequestException as e:
        print(f"Error fetching image keys: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    fetch_image_keys()
