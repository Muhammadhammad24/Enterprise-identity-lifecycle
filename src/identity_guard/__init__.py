class IdentityGuardPro:
    """Simple identity lifecycle manager demo class."""

    def new_employee_setup(self, data: dict) -> dict:
        required = {"first_name", "last_name", "email", "department", "start_date"}
        missing = sorted(required - set(data))
        if missing:
            return {"ok": False, "error": f"missing fields: {', '.join(missing)}"}
        return {"ok": True, "user": f"{data['first_name']} {data['last_name']}"}

    def offboard_employee(self, email: str) -> dict:
        if not email or "@" not in email:
            return {"ok": False, "error": "invalid email"}
        return {"ok": True, "message": f"User {email} successfully offboarded"}
