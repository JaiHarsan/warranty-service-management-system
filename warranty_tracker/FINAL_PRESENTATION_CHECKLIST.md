# Final Presentation Checklist

### Before Demo
- [ ] MongoDB running on local port 27017
- [ ] Virtual environment available (`venv`)
- [ ] Backend starts via `python backend/manage.py runserver`
- [ ] Frontend index HTML loads natively in browser
- [ ] Demo database seeded via `manage.py seed_demo`
- [ ] Demo credentials verified (`rahul@example.com` / `demo123`)
- [ ] Browser console checked (no silent unhandled Promise rejections)
- [ ] Screenshots captured (Dashboard, Health Check Engine, Service Appt)
- [ ] Documentation available in repository root
- [ ] Viva questions reviewed in `VIVA_QUESTIONS.md`

### During Demo
- [ ] Login
- [ ] Dashboard
- [ ] Product details inspection
- [ ] Warranty expiry visualization
- [ ] Health Check input selection
- [ ] Rule Result parsing
- [ ] Location calculation demonstration
- [ ] Service Centre list resolution
- [ ] Service Request local generation
- [ ] Logout

### If Something Fails
Use the documented fallback processes. If Mongo disconnects, restart the service. If coordinates block, show the fallback Search bar. Do not attempt live refactoring during the evaluation session.
