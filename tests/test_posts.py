import pytest
from typing import List
from app import schemas

def test_get_all_posts(authorized_client, test_posts):
    res = authorized_client.get("/posts")

    def validate(post):
        return schemas.PostOut(**post)
    posts_map = map(validate, res.json())
    posts_list = list(posts_map)
    print(posts_list)
    assert len(res.json()) == len(test_posts)
    assert res.status_code == 200
    # assert posts_list[0].Post.id == test_posts[0].id

def test_unauthorized_user_get_all_posts(client, test_posts):
    res = client.get("/posts")
    assert res.status_code == 401

def test_unauthorized_user_get_one_post(client, test_posts):
    res = client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_get_one_post_not_exist(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id + 100}")
    assert res.status_code == 404

def test_get_one_post(authorized_client, test_posts):
    res = authorized_client.get(f"/posts/{test_posts[0].id}")
    assert res.status_code == 200
    post = schemas.PostOut(**res.json())
    assert post.Post.id == test_posts[0].id

@pytest.mark.parametrize("title, content, published", [
    ("new title", "new content", True),
    ("another title", "another content", False),
    ("third title", "third content", True),
])
def test_create_post(authorized_client, test_user, title, content, published):
    res = authorized_client.post("/posts", json={"title": title, "content": content, "published": published})
    assert res.status_code == 201
    post = schemas.PostResponse(**res.json())
    assert post.title == title
    assert post.content == content
    assert post.owner_id == test_user["id"]

def test_create_post_default_published_true(authorized_client, test_user, test_posts):
    res = authorized_client.post("/posts", json={"title": "new title", "content": "new content"})
    assert res.status_code == 201
    post = schemas.PostResponse(**res.json())
    assert post.title == "new title"
    assert post.content == "new content"
    assert post.owner_id == test_user["id"]
    assert post.published == True

def test_unauthorized_user_create_post(client, test_posts):
    res = client.post("/posts", json={"title": "new title", "content": "new content"})
    assert res.status_code == 401

def test_unauthorized_user_delete_post(client, test_posts):
    res = client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 401

def test_delete_post_success(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id}")
    assert res.status_code == 204

def test_delete_post_non_exist(authorized_client, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[0].id + 100}")
    assert res.status_code == 404

def test_delete_post_not_owner(authorized_client, test_user, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code == 403 

def test_delete_other_user_post(authorized_client, test_posts):
    res = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert res.status_code == 403

def test_update_post(authorized_client, test_user, test_posts):
    data = {"title": "updated title", "content": "updated content", "published": True}
    res = authorized_client.put(f"/posts/{test_posts[0].id}", json=data)
    updated_post = schemas.PostResponse(**res.json())
    assert updated_post.title == data["title"]
    assert updated_post.content == data["content"]
    assert updated_post.published == data["published"]

def test_update_other_user_post(authorized_client, test_user, test_posts):
    data = {"title": "updated title", "content": "updated content", "published": True, "id": test_posts[3].id}
    res = authorized_client.put(f"/posts/{test_posts[3].id}", json=data)
    assert res.status_code == 403

def test_unauthorized_user_delete_post(client, test_user, test_posts):
    res = client.put(f"/posts/{test_posts[0].id}", json={"title": "updated title", "content": "updated content", "published": True})
    assert res.status_code == 401