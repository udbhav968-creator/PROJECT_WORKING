def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "online"
    assert "Udbhav" in data["module_owner"]


def test_admin_health(client):
    response = client.get("/api/v1/admin/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["database_connected"] is True


def test_seed_demo_data(client):
    response = client.post("/api/v1/admin/seed-demo-data")
    assert response.status_code == 200
    assert response.json()["success"] is True


def test_admin_dashboard_summary(client):
    # First seed data
    client.post("/api/v1/admin/seed-demo-data")
    
    response = client.get("/api/v1/admin/dashboard")
    assert response.status_code == 200
    data = response.json()
    assert data["success"] is True
    assert data["stats"]["total_users"] >= 1
    assert data["stats"]["total_appointments"] >= 2
    assert len(data["recent_logs"]) > 0
