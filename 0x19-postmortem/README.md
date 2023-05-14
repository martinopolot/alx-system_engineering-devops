# 0x19. Postmortem

Learning how to write a postmortem, which is also known as an incident report. This postmortem adheres closely to the rules utilized by Google engineers when filing reports. An issue summary, a timeline, a root cause analysis, a resolution and recovery section, and, finally, corrective and preventative measures, make up the report's five sections. Let's take a closer look at each of these elements.

[image](https://twitter.com/devopsreact/status/834887829486399488)

### Issue Summary

- Short summary (5 sentences)
- List the duration along with start and end times (include timezone)
- State the impact (most user requests resulted in 500 errors, at peak 100%)
- Close with root cause

### Timeline

- List the timezone
- Covers the outage duration
- When outage began
- When staff was notified
- Actions, - When service was restored

### Root Cause

- Explain in detail what was causing the issue
- Explain in detail how the issue was fixed and Do not sugarcoat

### Resolution and recovery

- Give a detailed explanation of actions taken (includes times)

### Corrective and Preventative Measures

- Itemized list of ways to prevent it from happening again
- What can we do better next time?

### Reporting format adapted from 
- The Google API Infrastructure Teamevents, 