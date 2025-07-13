#!/usr/bin/env python3
"""
KISS And tell
"""
import requests
import json

def test_endpoint(url, description):
    """Test an API endpoint and print results"""
    try:
        response = requests.get(url, timeout=5)
        print(f"\n{description}")
        print(f"URL: {url}")
        print(f"Status: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
        return True
    except Exception as e:
        print(f"\n{description}")
        print(f"URL: {url}")
        print(f"Error: {str(e)}")
        return False

def main():
    base_url = "http://localhost:8000"
    
    print("Testing API Endpoints")
    print("=" * 50)
    
    endpoints = [
        ("/", "Root and Heartbeat"),
        ("/health", "Health CSheck"),
        ("/api/universe", "Get Universe Map"),
        ("/api/universe/generate", "Generate Universe"),
        ("/api/universe/update", "Update Universe"),
        ("/api/game/status", "Game Status"),

    ]
    
    success_count = 0
    for endpoint, description in endpoints:
        if test_endpoint(f"{base_url}{endpoint}", description):
            success_count += 1
    
    print(f"\n{'='*50}")
    print(f"Results: {success_count}/{len(endpoints)} endpoints are working")
    
    if success_count == len(endpoints):
        print("Its Saul Good!")
    else:
        print("Failed - check the errors above")

if __name__ == "__main__":
    main()
