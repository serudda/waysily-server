# icough
Web application for doctors and patients, built on top of [drf-angular-user-system](https://github.com/si3792/drf-angular-user-system).

[Check it out here (Note that social login is disabled)](http://simoiliev.me/icough.html) 

### Index

3. [Setup](#setup)
2. [API](#api)
4. [Additional Configurations](#additional-configurations)
5. [Testing](#testing)
6. [Deployment considerations](#deployment-considerations)
7. [Further development notes](#further-development-notes)
8. [License](#license)


# Setup

Setup is identical to [drf-angular-user-system (setup and configuration)](https://github.com/si3792/drf-angular-user-system#setup-and-configuration).
Follow the steps there.  

Additionally, a `doctors` group needs to be created using Django admin.
Users are considered doctors if they are in the group. It is up to the server administrator to add
users to it, as this is only possible through the Django admin.

## API

### /icough/appointments/

API endpoint for Appointments

**GET** returns a list of UPCOMING appointments where:  
- If request comes from a patient, appointments where patient = user are returned.  
- If request comes from a doctor, appointments where doctor = user are returned.  

**POST** expects a a `time` field as well as `doctor` object field.  
( Doctor objects are retrieved from `/icough/doctors/` )

**PUT** is used to update appointment at `/icough/appointments/id/`  where:  
- If request comes from a doctor, `state` field is expected.  
- If request comes from a patient, `time` field is expected.

### /icough/history/

API endpoint for Appointments history

**GET** returns a list of EXPIRED appointments where:  
- If request comes from a patient, appointments where patient = user are returned.  
- If request comes from a doctor, appointments where doctor = user are returned.


### /icough/doctors/

Endpoint for fetching a list of doctors.  

**GET** returns an array of doctor objects.

## Additional configurations

### Changing the relative date cutoff value
Times for appointments that have happened (or are going to happen)
recently are showed as relative to the current moment.

 (eg 'a few seconds ago', 'in an hour', etc).

 You can modify `RELATIVE_DATE_CUTOFF_MINUTES` in `/client/app/controllers/appointments-table-controller/appointments-table-controller.js`
 to control the cutoff time for displaying datetimes as relative.
 
### Changing the appointment duration

Appointments are by default 30 minutes long. You can edit this value by setting `APPOINTMENT_DURATION`
in `server/project/icough/settings.py`.

### drf-angular-user-system

 Check out [drf-angular-user-system (additional configuration)](https://github.com/si3792/drf-angular-user-system#additional-configurations).

## Testing

Identical to [drf-angular-user-system (testing)](https://github.com/si3792/drf-angular-user-system#testing).

## Deployment considerations

Check out [drf-angular-user-system (deployment considerations)](https://github.com/si3792/drf-angular-user-system#deployment-considerations)
before deploying.

## Further development notes

- A lot of reduntant server calls are made using `AccountService`
for isDoctor checking. `AccountService` should be refactored to cache the requests.

- Saving events to calendar for Google users should be configurable (in /#/settings)

## License

Copyright 2016 Simo Iliev

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program. If not, see <http://www.gnu.org/licenses/>.
