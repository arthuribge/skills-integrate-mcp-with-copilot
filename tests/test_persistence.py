import json


def test_load_and_save_activities_persist_to_disk(tmp_path, monkeypatch):
    data_file = tmp_path / "activities.json"
    import src.app as app

    monkeypatch.setattr(app, "DATA_FILE", data_file)
    monkeypatch.setattr(app, "DATA_DIR", tmp_path)

    activities = app.load_activities()
    assert isinstance(activities, dict)
    assert "Chess Club" in activities

    activities["Chess Club"]["participants"].append("newstudent@mergington.edu")
    app.save_activities(activities)

    saved = json.loads(data_file.read_text())
    assert "newstudent@mergington.edu" in saved["Chess Club"]["participants"]
