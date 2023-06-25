import { Component } from '@angular/core';
import { DbsService } from '../../services/dbs.service';

@Component({
  selector: 'app-table-generic',
  templateUrl: './table-generic.component.html',
  styleUrls: ['./table-generic.component.css']
})
export class TableGenericComponent {
  race: string;
  constructor(private dbs: DbsService) {
    this.race = 'No Race'
    this.getData()
  }

  getData(): void {
    this.dbs.getRace().subscribe({
      next: response => {
        this.race = response;
        console.log(this.race)
      },
      error: (err: any) => {
        console.error(err)
      },
      complete: () => { }
    }
    )
  }

}
