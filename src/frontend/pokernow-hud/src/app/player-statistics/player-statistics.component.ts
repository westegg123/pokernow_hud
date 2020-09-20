import { Component, OnInit } from '@angular/core';
import { PlayerStatistic } from './PlayerStatistic'
// import { MOCK_STATS } from './mock-player-statistics'
import { PlayerStatisticsService } from './service/player-statistics.service'

@Component({
  selector: 'app-player-statistics',
  templateUrl: './player-statistics.component.html',
  styleUrls: ['./player-statistics.component.css']
})
export class PlayerStatisticsComponent implements OnInit {
  player_statistics: Set<PlayerStatistic>;

  constructor(private _player_statistics_service: PlayerStatisticsService) {
  	this.player_statistics = new Set<PlayerStatistic>();
  }

  ngOnInit(): void {
  	this.get_player_statistics("all");
  }

  get_player_statistics(player: String): void {
  	this._player_statistics_service.get_player_statistics(player).subscribe(new_player_statistics => {
  	  console.log(new_player_statistics);
  	  new_player_statistics.forEach(new_player_statistic => this.player_statistics.add(new_player_statistic))
      this.player_statistics.add(new_player_statistics);
  	  })
  	}
}
