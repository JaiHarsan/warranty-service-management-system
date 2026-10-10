# Viva Questions & Answers

**Q1: What is WarrantyCare?**
A: A full-stack web application designed to help consumers store warranties, predict product health based on rules, and book prototype service appointments before warranties expire.

**Q2: Why did you choose Vanilla JavaScript instead of React?**
A: To reduce node_modules bloat, deeply understand browser DOM APIs, and focus entirely on core business logic without the overhead of SPA frameworks for a mid-scale project.

**Q3: How is user authentication handled?**
A: Token-based authentication. The user submits credentials, the server validates against a PBKDF2 hashed password, and returns a secure token stored in localStorage. The `Authorization: Bearer <token>` header isolates user payloads.

**Q4: Why MongoDB over MySQL?**
A: MongoDB offers a flexible schema that allows seamless adaptation for varied product models (Laptops vs. Washing Machines have different health check criteria that map well to BSON).

**Q5: How does the Rule Engine work?**
A: It's a deterministic Python script (`rules.py`). It parses the submitted symptoms dictionary, evaluates categorical rules (like Overheating checks for Laptops), and categorizes them strictly as GREEN, YELLOW, or RED.

**Q6: What happens to OCR?**
A: Real OCR implies paid Cloud APIs. For the scope of a college project, an architectural skeleton is in place with a manual fallback acting as the current abstract processor.

**Q7: How is user data isolated?**
A: By extracting the User reference dynamically from the Bearer token via `get_user_from_request` inside DRF views. We never trust a `user_id` pushed from the client payload.

**Q8: Are the appointments real?**
A: No, they are prototype internal records mapped to a Service Centre to simulate an MVP flow.
