ALBUM_TITLE = "quidem molestiae enim"



def test_get_album_by_title(album_api):
    response = album_api.get_all()
    assert response.status_code == 200
    albums = response.json()
    for album in albums:
        if album["title"] == ALBUM_TITLE:
            album_from_list = album
            break
    album_by_id = album_api.get_by_id(album_from_list["id"]).json()
    assert album_by_id["title"] == album_from_list["title"]
    assert album_by_id["id"] == album_from_list["id"]
    assert album_by_id["userId"] == album_from_list["userId"]
