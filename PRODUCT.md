# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

## Users

Primary audience is the people evaluating the project: reviewers, employers, or teachers judging full-stack craft. They click through the product as a demo user: they register, build a profile, add friends, post, and join groups and channels. The product should feel like a working social network to them, not a tutorial scaffold.

## Product Purpose

A portfolio and learning project: a general-purpose social network built on Django. It succeeds when it shows solid, complete full-stack work, with coherent data modeling, permissions, and flows, and an interface that holds up when someone uses it.

## Positioning

Undecided. Today it is a straightforward Facebook/VK-style network with no claimed differentiator. Do not invent one in copy or design.

## Operating Context

- Server-rendered Django 5 templates (`templates/`) with a single base layout (`templates/base.html`). Own stylesheet and script live in `posts/static/` (`css/style.css`, `js/app.js`), the only static location Django finds without settings changes. Bootstrap Icons come from a CDN; Bootstrap CSS/JS is no longer used. Visual system: see DESIGN.md.
- SQLite in development; Docker image runs gunicorn with whitenoise static files.
- Users sign in with email. Staff get a link to the Django admin panel.

## Capabilities and Constraints

- **Accounts:** custom user model with email login, first/last name, birthday, and gender (man / female / other).
- **Profiles:** avatar (required), banner, bio, status, and display username.
- **Social graph:** mutual friendships, friend requests (send, accept, delete), and one-way subscriptions.
- **Posts:** title (max 50), body, optional media file, comments (max 250), likes, and reposts with optional text (max 80). Each post belongs to a profile, a group, or a channel.
- **Groups:** two-way communities with members and member admins; users can create, join, leave, and delete them.
- **Channels:** one-way broadcast spaces with viewers and viewer admins.
- **Terminology:** "Groups" (discussion), "Channels" (broadcast), "Friends", "Subscriptions", "Friend Requests".
- **Language:** the interface should support **Ukrainian and English** (i18n). This is not implemented yet: the UI copy is hardcoded English and no translation setup exists. Future UI work must leave room for Ukrainian strings, which often run longer.

## Evidence on Hand

- No real users, testimonials, metrics, or press. Never fabricate any of these.
- User-uploaded media lives in `media/` (avatars, banners, group/channel pictures, post media). Demo content comes from the local database only.
- README (Ukrainian) documents setup and admin login.

## Product Principles

1. **Complete over clever.** Every existing flow (create, edit, delete, confirm, empty, error) should work end to end before new features are added.
2. **Honest demo.** Show the product with real behavior and real data, with no fake stats or invented social proof.
3. **Clear social structures.** Users should always know whether they are acting in a profile, a group, or a channel, and what their role allows there.
4. **Bilingual by design.** Write copy and layouts so they hold up in both Ukrainian and English.
