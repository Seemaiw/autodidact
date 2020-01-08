import { Component, OnInit } from '@angular/core';
import {FormControl} from '@angular/forms';

@Component({
  selector: 'app-form-multiple',
  templateUrl: './form-multiple.component.html',
  styleUrls: ['./form-multiple.component.scss']
})
export class FormMultipleComponent implements OnInit {
  toppings = new FormControl();
  toppingList: string[] = ['Extra cheese', 'Mushroom', 'Onion', 'Pepperoni', 'Sausage', 'Tomato'];
  constructor() { }

  ngOnInit() {
  }

}
