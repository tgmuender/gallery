import { Component, OnInit, Input } from '@angular/core';
import { PreviewImage} from "../PreviewImage";

@Component({
  selector: 'app-image-detail',
  templateUrl: './image-detail.component.html',
  styleUrls: ['./image-detail.component.css']
})
export class ImageDetailComponent implements OnInit {

  @Input() image: PreviewImage;

  constructor() { }

  ngOnInit() {
  }

}
