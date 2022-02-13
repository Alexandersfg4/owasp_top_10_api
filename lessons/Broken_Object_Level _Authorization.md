# Broken Object Level Authorization

Broken Object Level Authorization happens when an application does not correctly confirm that the user performing the request has the required privileges to access a resource of another user. Almost every company has APIs that are vulnerable to BOLA.

Object level authorization is an access control mechanism that is usually implemented at the code level to validate that one user can only access objects that they should have access to. An object is any information to which the application has access.

When an application includes a BOLA or IDOR vulnerability the application has a strong probability of exposing sensitive information or data to attackers. Once recognized, BOLA vulnerabilities can be exceptionally easy to exploit, frequently using simple scripting.

All the attackers need to do is to exchange the ID of their own resource in the API call with an ID of a resource belonging to another user. The absence of proper authorization checks enables hackers to access the specified resource. This attack is also known as IDOR (Insecure Direct Object Reference).

## There are two main types of Broken Object Level Authorization (BOLA):
- Based on user ID
- Based on object ID

### Based on user ID
The API endpoints receive a user ID and access the user object based on this ID. For example:

``` /api/trips/get_all_trips_for_user?user_id=777```

t’s usually easier to solve this type of BOLA because the authorization mechanism is straightforward — the developers simply fetch the ID of the logged-in user from the session (e.g.: `current_user.id`), and compare it with user_id from the GET parameter.

Things get more complicated when one user is supposed to manage other users by design (for example sub-users, regional manager, etc)

### Based on object ID
The API endpoint receives an ID of an object which is not a user object. For example: 

```/api/trips/receipts/download_as_pdf?receipt_id=1111```

The reasons why we end up having Broken Object Level Authorization (BOLA) vulnerabilities in the code are quite simple: the lack of security control and human error. For example, an API that handles both sensitive and non-sensitive data. Some requests should have authorization checks and others shouldn’t therefore it’s easy to miss a check when writing code.
