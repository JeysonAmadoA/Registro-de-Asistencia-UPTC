import { TestBed } from '@angular/core/testing';

import { ProccessDataService } from './proccess-data.service';

describe('ProccessDataService', () => {
  let service: ProccessDataService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ProccessDataService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
