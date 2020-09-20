import { Injectable } from '@angular/core';
import { Observable, of } from 'rxjs';
import { map } from 'rxjs/operators';
import { PlayerStatistic } from '../PlayerStatistic'
import { HttpClient, HttpHeaders } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class PlayerStatisticsService {

  constructor(private http_client: HttpClient) {}

  get_player_statistics(player: String): Observable<PlayerStatistic> {
    let ps = this.http_client.get<PlayerStatistic>("http://localhost:5000/api/statistics/".concat(player));
    console.log(ps);
  	return ps;
  }

}
