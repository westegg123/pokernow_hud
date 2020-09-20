import { TestBed } from '@angular/core/testing';

import { PlayerStatisticsService } from './player-statistics.service';

describe('PlayerStatisticsService', () => {
  let service: PlayerStatisticsService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(PlayerStatisticsService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
