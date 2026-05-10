from trail_video_geolocation import geolocate_video

def test_geolocate_video():
    c = geolocate_video("footage.mp4")
    assert "estimated_lat" in c.result
    assert c.result["radius_km"] > 0
