import { uploadPhoto, createUser } from './utils';

export default async function asyncUploadUser() {
  let photoUp;
  let userUp;
  try {
    photoUp = await uploadPhoto();
    userUp = await createUser();
  } catch (e) {
    photoUp = null;
    userUp = null;
  }
  return { photo: photoUp, user: userUp };
}
