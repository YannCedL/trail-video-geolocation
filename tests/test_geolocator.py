# test de la géolocalisation de trajectoire vidéo Trail
from trail_video_geolocation.geolocator import geolocate_video

def test_geolocate_video():
    contract = geolocate_video("parcours_drone.mp4")
    assert contract is not None
    assert len(contract.result["trajectory"]) >= 1
    assert contract.result["total_distance_meters"] > 0
    assert len(contract.evidence) >= 1
