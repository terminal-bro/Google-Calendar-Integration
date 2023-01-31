# Django Google Calendar Integration
----

## 1. Init



![](https://developers.google.com/workspace/images/auth-overview.png)

Refer [Google OAuth Documentation](https://developers.google.com/identity/protocols/oauth2/web-server#python_1)

1. Creates an instance of google_auth_oauthlib.flow.Flow by reading the client secrets from a specified file.
2. Sets the redirect URI to a specified URL, which must match one of the authorized redirect URIs for the OAuth 2.0 client.
3. Generates an authorization URL and a state, which is used to initiate the OAuth 2.0 authorization grant flow.
4. Stores the state in the session so that it can be verified in the authorization server response.
5. Returns a Response object with the authorization URL as its content.

## 2. Redirect

1. Starts by retrieving the state from the session and creating an OAuth2 flow object with the specified client secrets file and scopes.
2. Exchanges the authorization code in the authorization server's response for OAuth 2.0 tokens using the "fetch_token" method of the flow object.
3. Resulting credentials object is saved to the session in a dictionary form. 
4. Saved credentials are then loaded from the session and used to build a client library for the Google Calendar API.
5. Fetches the calendar list for the user and retrieves the first calendar in the list
## Problems likely to face

1. [KeyError: 'client_secret'](https://stackoverflow.com/questions/66837819/issue-with-google-drive-api-keyerror-client-secret)

2. Enable the Calendar API in Cloud Console


## [CalDAV API](https://developers.google.com/calendar/api/v3/reference?apix=true)
---
   
    The CalDAV API lets you manage your Google calendars and events.


# Resources List
---

- [Google API Documentation](https://developers.google.com/identity/protocols/oauth2/web-server#python_1)
- [Google OAuth Python Client Library](https://googleapis.github.io/google-api-python-client/docs/oauth.html)
- [Goole Calendar](https://developers.google.com/calendar/caldav/v2/auth)
- [Google OAuth Consent](https://developers.google.com/workspace/guides/configure-oauth-consent)
- [Google Calendar API Overview](https://developers.google.com/calendar/api/guides/overview)
- [Google Calendar Python](https://developers.google.com/calendar/api/quickstart/python)
- [Get events](https://developers.google.com/calendar/api/v3/reference/calendarList/list)
- [Relevant Blog post](https://rx-36.life/post/data-communication-between-django-and-google-calendar-api/)
- [OAuth Protocol](https://www.rfc-editor.org/rfc/rfc6749) 




