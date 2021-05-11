import { uploadPhoto, createUser } from './utils';

export default function handleProfileSignup() {
  const promises = [uploadPhoto(), createUser()];
  return Promise.all(promises)
    .then((data) => console.log(`${data[0].body} ${data[1].firstName} ${data[1].lastName}`))
    .catch(() => console.log('Signup system offline'));
}
