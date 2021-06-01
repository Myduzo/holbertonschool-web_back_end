import createPushNotificationsJobs from './8-job.js';
import { expect } from 'chai';

const kue = require('kue');
const queue = kue.createQueue();

const jobList = [
  {phoneNumber: '31256416', message: 'phoneNumber 1'},
  {phoneNumber: '31258945', message: 'phoneNumber 2'},
  {phoneNumber: '31251234', message: 'phoneNumber 3'},
  {phoneNumber: '31257891', message: 'phoneNumber 4'}
];

before(() => {
  queue.testMode.enter();
});

afterEach(() => {
  queue.testMode.clear();
});

after(() => {
  queue.testMode.exit();
});

describe('createPushNotificationsJobs', () => {
  it('valid phoneNumbers', () => {
    createPushNotificationsJobs(jobList, queue);
    expect(queue.testMode.jobs.length).to.equal(4);
    createPushNotificationsJobs(jobList, queue);
    expect(queue.testMode.jobs.length).to.equal(8);
    createPushNotificationsJobs(jobList, queue);
    expect(queue.testMode.jobs.length).to.equal(12);
  });

  it('invalid phoneNumbers', () => {
    expect(() => createPushNotificationsJobs(NaN, queue).to.throw(Error));
    expect(() => createPushNotificationsJobs('', queue).to.throw(Error));
    expect(() => createPushNotificationsJobs(1235846, queue).to.throw(Error));
  });
});