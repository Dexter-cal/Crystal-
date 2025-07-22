# Cross-Site Request Forgery (CSRF)

## What is Cross-Site Request Forgery?

Cross-Site Request Forgery (CSRF) is an attack that forces an end user to execute unwanted actions on a web application in which they're currently authenticated. CSRF attacks specifically target state-changing requests, not theft of data, since the attacker has no way to see the response to the forged request.

## Example

A simple example of CSRF is to create a web page with an image tag that has a malicious URL as the source. For example:

```html
<img src="http://example.com/transfer?to=attacker&amount=1000">
```

If a user who is authenticated to `example.com` visits this page, their browser will automatically send a request to the malicious URL, transferring 1000 to the attacker.
