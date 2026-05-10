from trail_video_geolocation.geolocator import geolocate_video

def test_geolocate_video():
    c = geolocate_video("footage.mp4")
    assert "estimated_start_point" in c.result
    assert c.result["total_distance_meters"] > 0
