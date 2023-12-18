t sinon = require('sinon');
const { expect } = require('chai');
const kue = require('kue');
const { beforeEach, afterEach, it, describe } = require('mocha');
const { createPushNotificationsJobs } = require('./8-job');

describe('createPushNotificationsJobs', () => {
	  let queue;
	  let testJobs;

	  beforeEach(() => {
	    // Arrange
	    queue = kue.createQueue();
	    testJobs = [
	      { phoneNumber: '1234567890', message: 'Message 1' },
	      { phoneNumber: '0987654321', message: 'Message 2' },
	    ];
	  });

	  afterEach(() => {
	    // Clean up
	    queue.shutdown();
	  });

	  it('should create jobs for each item in the jobs array', (done) => {
	    // Arrange
            const createSpy = sinon.spy(queue, 'create');

	    // Act
            createPushNotificationsJobs(testJobs, queue);

           // Assert
           setTimeout(() => {
		         expect(createSpy.callCount).to.equal(testJobs.length);
		         testJobs.forEach((jobData, index) => {
				         expect(createSpy.getCall(index).args[0]).to.equal('push_notification_code_3');
				         expect(createSpy.getCall(index).args[1]).to.equal(jobData);
				       });
		         done();
		       }, 10); // Adjust the delay as needed
		    });
