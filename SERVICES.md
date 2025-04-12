# Complete E-commerce API Reference (Django + DRF)

## 1. **Users App** (`/api/users/`)
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/register/` | POST | Create new user | ❌ |
| `/login/` | POST | JWT token pair | ❌ |
| `/me/` | GET | Get user profile | ✅ |
| `/me/` | PUT | Update profile | ✅ |
| `/addresses/` | GET | List user addresses | ✅ |
| `/addresses/` | POST | Add new address | ✅ |
| `/addresses/<id>/` | PUT | Update address | ✅ |
| `/addresses/<id>/` | DELETE | Remove address | ✅ |

## 2. **Products App** (`/api/products/`)
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/` | GET | List all products (filter/search) | ❌ |
| `/` | POST | Create product | Admin |
| `/<slug>/` | GET | Product details | ❌ |
| `/<slug>/` | PUT | Update product | Admin |
| `/<slug>/` | DELETE | Delete product | Admin |
| `/categories/` | GET | List categories | ❌ |
| `/categories/` | POST | Create category | Admin |
| `/<slug>/reviews/` | GET | List reviews | ❌ |
| `/<slug>/reviews/` | POST | Add review | ✅ |

## 3. **Cart App** (`/api/cart/`)
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/` | GET | Get cart items | ✅ |
| `/` | POST | Add to cart | ✅ |
| `/items/<id>/` | PUT | Update quantity | ✅ |
| `/items/<id>/` | DELETE | Remove item | ✅ |
| `/clear/` | POST | Empty cart | ✅ |

## 4. **Orders App** (`/api/orders/`)
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/` | GET | List user orders | ✅ |
| `/` | POST | Create order | ✅ |
| `/<order_id>/` | GET | Order details | ✅ |
| `/<order_id>/cancel/` | POST | Cancel order | ✅ |
| `/checkout/` | POST | Initiate payment | ✅ |

## 5. **Payments App** (`/api/payments/`)
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/` | POST | Process payment | ✅ |
| `/verify/` | POST | Verify payment | ✅ |
| `/history/` | GET | Payment history | ✅ |
| `/webhook/<gateway>/` | POST | Payment webhook | ❌ |

## 6. **Coupons App** (`/api/coupons/`)
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/` | GET | List active coupons | ❌ |
| `/` | POST | Create coupon | Admin |
| `/<code>/` | GET | Check coupon validity | ❌ |
| `/<code>/apply/` | POST | Apply to cart | ✅ |

## 7. **Support App** (`/api/support/`)
| Endpoint | Method | Description | Auth Required |
|----------|--------|-------------|---------------|
| `/tickets/` | GET | List user tickets | ✅ |
| `/tickets/` | POST | Create ticket | ✅ |
| `/tickets/<id>/` | GET | Ticket details | ✅ |
| `/tickets/<id>/close/` | POST | Close ticket | ✅ |
| `/contact/` | POST | Submit contact form | ❌ |

## 8. **Analytics App** (`/api/analytics/`) *(Admin-only)*
| Endpoint | Method | Description |
|----------|--------|-------------|
| `/sales/` | GET | Sales reports |
| `/top-products/` | GET | Best sellers |
| `/user-activity/` | GET | User behavior |