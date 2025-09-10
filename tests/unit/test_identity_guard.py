from identity_guard import IdentityGuardPro

def test_new_employee_setup_ok():
    mgr = IdentityGuardPro()
    out = mgr.new_employee_setup({
        "first_name": "John",
        "last_name": "Doe",
        "email": "john.doe@company.com",
        "department": "Engineering",
        "start_date": "2024-01-15",
    })
    assert out["ok"] is True
    assert out["user"] == "John Doe"
