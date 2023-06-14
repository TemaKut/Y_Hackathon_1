import React from 'react';

import Style from './Main.module.scss';
import Cell from '../Cell/Cell';

function Main() {
  return (
    <main className={Style.main}>
      <Cell />
    </main>
  );
}

export default Main;
