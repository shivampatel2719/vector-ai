import { swapCards } from "./api-services"

export async function onDragEnd(result, columns, setColumns) {
  if (!result.destination) return;
  const { source, destination } = result;
  const tempItems = columns[source.droppableId]['items'];
  columns[source.droppableId]['items'] = [...columns[destination.droppableId]['items']];
  columns[destination.droppableId]['items'] = [...tempItems];
  let obj = {
    "id1" : source.droppableId, "id2" : destination.droppableId
  }
  await swapCards(obj);
  setColumns(columns);
};

export const modifyData = (columns,data) => {
    Object.entries(data).forEach(([key,value]) => {
        if(columns[(value['position']).toString()] && columns[(value['position']).toString()]['items']) {
          value['id'] = value['id'].toString();
          columns[(value['position']).toString()]['items'] = [(value)];
        }
    });
    return columns;
};
