# Cross-Site Scripting (XSS)

## What is Cross-Site Scripting?

Cross-Site Scripting (XSS) is a type of security vulnerability typically found in web applications. XSS attacks enable attackers to inject client-side scripts into web pages viewed by other users. A cross-site scripting vulnerability may be used by attackers to bypass access controls such as the same-origin policy.

## Example

A simple example of XSS is to enter `<script>alert('XSS')</script>` in a comment field. If the application is vulnerable, this will cause the script to be executed in the browser of any user who views the comment.
