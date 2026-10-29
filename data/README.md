# Data

Tables from the *Maven Fuzzy Factory* e-commerce dataset (Maven Analytics), a public, fictional dataset for analytics
training. It covers an online stuffed-toy retailer from March 2012 to March 2015. Files ending in `.csv.gz` are
gzip-compressed CSVs; pandas reads them directly. The data are unchanged from the source except for compression.

## `products.csv` (4 rows)

| Column | Description |
|---|---|
| `product_id` | Product identifier |
| `created_at` | Launch date |
| `product_name` | Product name |

## `order_items.csv` (40,025 rows, one per item)

| Column | Description |
|---|---|
| `order_item_id` | Item identifier |
| `created_at` | Order timestamp |
| `order_id` | Order identifier |
| `product_id` | Product identifier |
| `is_primary_item` | 1 for the first item added, 0 for cross-sold items |
| `price_usd`, `cogs_usd` | Item revenue and cost (USD) |

## `order_item_refunds.csv` (1,731 rows)

| Column | Description |
|---|---|
| `order_item_refund_id` | Refund identifier |
| `created_at` | Refund timestamp |
| `order_item_id`, `order_id` | Refunded item and its order |
| `refund_amount_usd` | Amount refunded (USD) |

## `website_sessions.csv.gz` (472,871 rows, one per session)

| Column | Description |
|---|---|
| `website_session_id` | Session identifier |
| `created_at` | Session start |
| `user_id` | Anonymous visitor identifier |
| `is_repeat_session` | 1 if the visitor had a previous session |
| `utm_source`, `utm_campaign`, `utm_content` | Paid-traffic tags; empty for untagged traffic |
| `device_type` | `desktop` or `mobile` |
| `http_referer` | Referring site; empty for direct type-in traffic |

## `website_pageviews.csv.gz` (1,188,124 rows, one per page view)

| Column | Description |
|---|---|
| `website_pageview_id` | Page-view identifier (increases with time) |
| `created_at` | Timestamp |
| `website_session_id` | Session identifier |
| `pageview_url` | Page path, for example `/products`, `/cart`, `/thank-you-for-your-order` |
