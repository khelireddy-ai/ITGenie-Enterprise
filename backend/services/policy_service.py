from services.llm_service import ask_llm
from database import get_connection


def generate_policy(policy_name, policy_type, purpose):

    prompt = f"""
You are an ISO 27001 Information Security expert.

Generate a professional company policy.

Policy Name:
{policy_name}

Policy Type:
{policy_type}

Purpose:
{purpose}

Include

1 Purpose
2 Scope
3 Roles and Responsibilities
4 Policy Statements
5 Exceptions
6 References
"""

    policy = ask_llm(prompt, "")

    conn = get_connection()

    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO policies
        (policy_name, policy_type, purpose, content)
        VALUES (?,?,?,?)
        """,
        (
            policy_name,
            policy_type,
            purpose,
            policy,
        ),
    )

    conn.commit()
    conn.close()

    return policy
